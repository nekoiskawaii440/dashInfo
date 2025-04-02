import axios from "axios";

const API_BASE_URL = "http://localhost:8000";

export const fetchData = async (city: string) => {
    const response = await axios.get(`${API_BASE_URL}/`, {
        params: { city },
      });
      return response.data;
};