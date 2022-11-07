import axios from "axios";

export function createRequestInstance(config) {
  const instance = axios.create({
    withCredentials: true,
    headers: {
      Accept: "application/json",
    },
    ...config,
  });

  instance.interceptors.request.use(
    async function (config) {
      return config;
    },
    function (error) {
      return Promise.reject(error);
    }
  );

  // Add a response interceptor
  instance.interceptors.response.use(
    function (response) {
      return response.data;
    },
    function (error) {
      return Promise.reject(error);
    }
  );

  return instance;
}
