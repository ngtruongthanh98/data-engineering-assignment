import axios from "axios";

export const getGames = () => {
  const url = "http://localhost:5000/games";
  return axios.get(url);
};
