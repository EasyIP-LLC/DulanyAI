"use client";
import { Navbar } from "../_components/navbar/navbar";
import { Footer } from "../_components/footer/footer";
import { Summary } from "../_components/summary/summary";
import "./home.css";

export default function Home() {
  console.log(process.env.AUTH0_SECRET);
  console.log(process.env.AUTH0_BASE_URL);
  console.log(process.env.AUTH0_ISSUER_BASE_URL);
  console.log(process.env.AUTH0_CLIENT_ID);
  console.log(process.env.AUTH0_CLIENT_SECRET);

  return (
    <>
      <div className="snap-scroll-container">
        <Navbar />
        <div
          className="div-view custom-padding custom-background"
          style={
            {
              "--custom-padding-top": "10%",
              "--custom-background-color": "#F5EFE6",
            } as React.CSSProperties
          }
        >
          <Summary />
        </div>
      </div>
      <Footer />
    </>
  );
}
