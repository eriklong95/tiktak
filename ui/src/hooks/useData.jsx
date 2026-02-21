import { useEffect, useState } from "react";

function useData(url) {
    const [data, setData] = useState(null);
    useEffect(() => {
        fetch(new Request(url))
          .then(response => response.json())
          .then(json => {
              setData(json);
          });
    }, [url]);
    return data;
  }

export default useData;
