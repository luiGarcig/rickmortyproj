import styled, { keyframes } from "styled-components";

const fadeIn = keyframes`
  from { opacity: 0; transform: translateY(10px); }
  to   { opacity: 1; transform: translateY(0); }
`;

export const Overlay = styled.div`
  position: fixed;
  inset: 0;
  display: flex;
  justify-content: center;
  align-items: center;
  z-index: 2000;
`;

export const ModalWrapper = styled.div`
  position: relative;
  width: 70%;
  height: 80vh;
  display: flex;
  align-items: center;
`;
export const LeftCard = styled.div`
  position: absolute;
  border-radius: 10px;
  border: 2px solid rgba(255, 255, 255, 0.1);
  width: 28%; 
  height: 75%;
  left: -20px; 
  z-index: 20; 
  box-shadow: 0 20px 40px rgba(0,0,0,0.5);
  display: flex;
  flex-direction: column;
`;

export const CharacterImage = styled.img`
  width: 100%;
  height: 100%; 
  flex: 1;
  object-fit: cover;
  border-radius: 10px 10px 0 0;
`;

export const CardInfo = styled.div`
  background: #1f1f1f; 
  padding: 5px;
  border-radius: 0 0 10px 10px;
  color: white;
`;

export const ContentCard = styled.div`
  display: flex;
  width: 100%;
  height: 90%;
  margin-left: 8%;
  border-radius: 10px;
  overflow: hidden;
  position: relative;
`;

export const LeftSection = styled.div`
  background: rgba(0,0,0,0.5);
  backdrop-filter: blur(15px);
  width: 30%;
  height: 100%;
  border-right: 1px solid rgba(255, 255, 255, 0.05);
  display: flex;
  align-items: flex-start; 
  position: relative;
`;

export const CloseButton = styled.button`
  margin: 10px;
  padding: 8px 16px;
  border-radius: 8px;
  background: rgba(255, 255, 255, 0.1);
  border: 1px solid rgba(255, 255, 255, 0.2);
  color: white;
  cursor: pointer;
  z-index: 50;
  transition: 0.2s;

  &:hover {
    background: white;
    color: black;
  }
`;

export const RightSection = styled.div`
  padding: 40px;
  overflow-y: auto;
  background: #0b0b0b;
  width: 70%;
  height: 100%;
`;


export const Name = styled.h1` font-size: 20px; font-weight: 800; margin: 0; color: white; line-height: 1.1; `;
export const Species = styled.p` font-size: 16px; color: #a0a0a0; margin: 4px 0 0 0; `;
export const Section = styled.div` margin-bottom: 32px; `;
export const SectionTitle = styled.h3` color: #d2ff5e; font-size: 13px; letter-spacing: 1.5px; text-transform: uppercase; margin-bottom: 12px; font-weight: 700; `;
export const DescriptionText = styled.p` font-size: 15px; line-height: 1.6; color: #d1d5db; `;
export const Label = styled.p` color: #6b7280; font-size: 12px; margin-bottom: 4px; text-transform: uppercase; `;
export const Value = styled.p` font-size: 20px; font-weight: 600; color: #ffffff; margin: 0; `;
export const SubValue = styled.p` font-size: 14px; color: #9ca3af; margin-top: 2px; `;
export const Residents = styled.div` display: inline-flex; align-items: center; margin-top: 8px; font-size: 13px; color: #9ca3af; background: rgba(255, 255, 255, 0.05); padding: 4px 8px; border-radius: 4px; `;;
