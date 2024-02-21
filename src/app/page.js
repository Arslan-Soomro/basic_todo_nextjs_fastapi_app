"use client"

import Image from "next/image";
import { useEffect } from "react";

export default function Home() {

  useEffect(() => {
    (async () => {
      const data = await fetch("/api/todos");
      const json = await data.json();
      console.log("Data: ", json);
    })()
  }, []);

  return (
    <div>Hello World</div>
  );
}
