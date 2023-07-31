import React, { createContext, useState, useEffect } from "react"; //diff b/w createContext and UseContext?
export const DataContext = createContext();

function DataContextProvider(props) {
  const [formData, setFormData] = useState({});
  useEffect(() => {}, []);

  return (
    <DataContext.Provider
      value={{
        formData,
        setFormData,
      }}
    >
      {props.children}
    </DataContext.Provider>
  );
}
export default DataContextProvider;
