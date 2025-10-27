import json
import os
import re
from pathlib import Path

import psycopg2
from psycopg2.extras import execute_batch

DATA_DIR = Path(__file__).parent  
LOCATIONS_JSON = DATA_DIR / "allLocations (1).json"
EPISODES_JSON = DATA_DIR / "allEpisodesUpdated (1).json"
CHARACTERS_JSON = DATA_DIR / "allCharsUpdated (3) (2).json"

PGHOST = os.getenv("PGHOST", "localhost")
PGPORT = int(os.getenv("PGPORT", "5432"))
PGUSER = os.getenv("PGUSER", "postgres")
PGPASSWORD = os.getenv("PGPASSWORD", "postgres")
PGDATABASE = os.getenv("PGDATABASE", "rickmorty")

URL_ID_RE = re.compile(r".*/(\d+)$")

def get_id_from_url(url: str | None) -> int | None:
    if not url or not isinstance(url, str):
        return None
    m = URL_ID_RE.match(url.strip())
    return int(m.group(1)) if m else None


def connect():
    return psycopg2.connect(
        host=PGHOST, port=PGPORT, user=PGUSER, password=PGPASSWORD, dbname=PGDATABASE
    )


SCHEMA_SQL = """
CREATE TABLE IF NOT EXISTS locations (
    id              INTEGER PRIMARY KEY,
    name            TEXT NOT NULL,
    type            TEXT,
    dimension       TEXT
);

CREATE TABLE IF NOT EXISTS episodes (
    id        INTEGER PRIMARY KEY,
    name      TEXT NOT NULL,
    air_date  TEXT,
    episode   TEXT
);

CREATE TABLE IF NOT EXISTS characters (
    id          INTEGER PRIMARY KEY,
    name        TEXT NOT NULL,
    status      TEXT,
    species     TEXT,
    type        TEXT,
    gender      TEXT,
    image       TEXT,
    origin_id   INTEGER REFERENCES locations(id) ON DELETE SET NULL,
    location_id INTEGER REFERENCES locations(id) ON DELETE SET NULL
);

CREATE TABLE IF NOT EXISTS characters_episodes (
    episode_id   INTEGER REFERENCES episodes(id)   ON DELETE CASCADE,
    character_id INTEGER REFERENCES characters(id) ON DELETE CASCADE,
    PRIMARY KEY (episode_id, character_id)
);
"""


def load_json(path: Path):
    with open(path, "r", encoding="utf-8") as f:
        return json.load(f)


def seed_locations(cur):
    data = load_json(LOCATIONS_JSON)
    rows = []
    for loc in data:
        rows.append(
            (
                int(loc["id"]),
                loc.get("name"),
                loc.get("type"),
                loc.get("dimension"),
            )
        )
    sql = """
        INSERT INTO locations (id, name, type, dimension)
        VALUES (%s, %s, %s, %s)
        ON CONFLICT (id) DO UPDATE
        SET name=EXCLUDED.name,
            type=EXCLUDED.type,
            dimension=EXCLUDED.dimension;
        """
    execute_batch(cur, sql, rows, page_size=500)


def seed_episodes(cur):
    data = load_json(EPISODES_JSON)
    rows = []
    for ep in data:
        rows.append(
            (
                int(ep["id"]),
                ep.get("name"),
                ep.get("air_date"),
                ep.get("episode"),
            )
        )
    sql = """
        INSERT INTO episodes (id, name, air_date, episode)
        VALUES (%s, %s, %s, %s)
        ON CONFLICT (id) DO UPDATE
        SET name=EXCLUDED.name,
            air_date=EXCLUDED.air_date,
            episode=EXCLUDED.episode;
    """
    execute_batch(cur, sql, rows, page_size=500)


def seed_characters_and_links(cur):
    data = load_json(CHARACTERS_JSON)


    char_rows = []
    link_rows = []
    for ch in data:
        origin_id = get_id_from_url((ch.get("origin") or {}).get("url"))
        location_id = get_id_from_url((ch.get("location") or {}).get("url"))
        char_rows.append(
            (
                int(ch["id"]),
                ch.get("name"),
                ch.get("status"),
                ch.get("species"),
                ch.get("type") or None,
                ch.get("gender"),
                ch.get("image"),
                origin_id,
                location_id,
            )
        )


        for ep_url in ch.get("episode", []) or []:
            ep_id = get_id_from_url(ep_url)
            if ep_id:
                link_rows.append((ep_id, int(ch["id"])))

    sql_chars = """
        INSERT INTO characters
            (id, name, status, species, type, gender, image, origin_id, location_id)
        VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s)
        ON CONFLICT (id) DO UPDATE
        SET name=EXCLUDED.name,
            status=EXCLUDED.status,
            species=EXCLUDED.species,
            type=EXCLUDED.type,
            gender=EXCLUDED.gender,
            image=EXCLUDED.image,
            origin_id=EXCLUDED.origin_id,
            location_id=EXCLUDED.location_id;
    """
    execute_batch(cur, sql_chars, char_rows, page_size=500)


    sql_links = """
        INSERT INTO characters_episodes (episode_id, character_id)
        VALUES (%s, %s)
        ON CONFLICT DO NOTHING;
    """
    if link_rows:
        execute_batch(cur, sql_links, link_rows, page_size=1000)


def main():

    for p in (LOCATIONS_JSON, EPISODES_JSON, CHARACTERS_JSON):
        if not Path(p).exists():
            raise SystemExit(f"Arquivo não encontrado: {p}")

    with connect() as conn:
        conn.autocommit = False
        with conn.cursor() as cur:
            print("-> criando/atualizando esquema…")
            cur.execute(SCHEMA_SQL)

            print("-> carregando locations…")
            seed_locations(cur)

            print("-> carregando episodes…")
            seed_episodes(cur)

            print("-> carregando characters e vínculos…")
            seed_characters_and_links(cur)

        conn.commit()
        print("✅ pronto! Dados inseridos/atualizados.")


if __name__ == "__main__":
    main()
