import axios from "axios";

export const getComments = () => {
  const url = "http://localhost:5000/comments";
  return axios.get(url);
};
