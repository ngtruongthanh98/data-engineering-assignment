import axios from "axios";

export const getComments = (queryParams) => {
  const url = "http://localhost:5000/comments";
  return axios.get(url, { params: queryParams });
};
