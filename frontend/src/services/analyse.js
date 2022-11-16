import axios from "axios";

export const getDescriseTable = (tableName) => {
  const url = `http://localhost:5000/overview/${tableName}`;
  return axios.get(url);
};
