import axios from "axios";

export const getProducts = () => {
  // ! Change API for testing
  const url = "http://localhost:5000/games";
  return axios.get(url);
};
