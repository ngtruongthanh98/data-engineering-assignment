import axios from "axios";

export const getProducts = (queryParams) => {
  const url = "http://localhost:5000/products";
  return axios.get(url, { params: queryParams });
};

export const getCategories = () => {
  const url = "http://localhost:5000/categories";
  return axios.get(url);
};
