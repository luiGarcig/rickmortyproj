import React from "react";
import { Input } from "./styles";


interface SearchInputProps extends React.InputHTMLAttributes<HTMLInputElement> {}

export const SearchInput: React.FC<SearchInputProps> = (props) => {
  return (
    <Input {...props} />
  );
};
