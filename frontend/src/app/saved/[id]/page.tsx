"use client";
import { useParams } from "next/navigation";
import React, { useState, useEffect } from "react";
import { Navbar } from "@/_components/navbar/navbar";
import { Footer } from "@/_components/footer/footer";
import styles from "./styles.module.css";

interface PatentInfo {
  abstract: string;
  alias: string;
  id: string;
  image: string;
  index: string;
  inventors: string[];
  mapping: any;
  owner: string;
  publication_date: string;
  publication_id: string;
  score: number;
  snippet: string | null;
  title: string;
  type: string;
  www_link: string;
}

interface Citations {
  [key: string]: {
    abstract: { before: string; highlight: string; after: string }[];
    claims: { before: string; highlight: string; after: string }[];
    description: string | null;
  };
}

interface Percentages {
  [key: string]: number;
}

interface Patent {
  patentInfo: PatentInfo;
  search: string;
  citations: Citations;
  percentages: Percentages;
}

const Page = () => {
  const [patent, setPatent] = useState<Patent | null>(null);
  const params = useParams();

  useEffect(() => {
    const fetchSavedPatents = async () => {
      try {
        const response = await fetch("/api/fetch_one_patent", {
          method: "POST",
          headers: {
            "Content-Type": "application/json",
          },
          body: JSON.stringify({
            patent_neon_id: params.id,
          }),
        });
        const data = await response.json();
        console.log("patent-data:", data);
        setPatent(data.patent);
      } catch (error) {
        console.error("Error fetching saved patents:", error);
      }
    };
    fetchSavedPatents();
  }, [params.id]);

  if (!patent) {
    return <div>Loading...</div>;
  }

  const { patentInfo, search, citations, percentages } = patent;

  return (
    <>
      <div className={styles.coloredDiv}>
        <Navbar />
        <div className={`${styles.infoPanel} ${styles.animationContainer}`}>
          <div className={styles.patentDetails}>
            <h1 className={styles.patentTitle}>{patentInfo.title}</h1>
            <p><strong>Inventors:</strong> {patentInfo.inventors.join(', ')}</p>
            <p><strong>Owner:</strong> {patentInfo.owner}</p>
            <p><strong>Publication Date:</strong> {new Date(patentInfo.publication_date).toLocaleDateString()}</p>
            <p><strong>Abstract:</strong> {patentInfo.abstract}</p>
            <p><strong>Search Term:</strong> {search}</p>
            <div>
              <a href={patentInfo.www_link} target="_blank" rel="noopener noreferrer">View on Google Patents</a>
            </div>
          </div>
          <div className={styles.percentages}>
            <h3>Feature Percentages</h3>
            <ul>
              {percentages && Object.entries(percentages).map(([feature, percentage]) => (
                <li key={feature}>{feature} --- {(percentage * 100).toFixed(2)}%</li>
              ))}
            </ul>
          </div>
          {/* <div className={styles.citations}>
            <h3>Citations</h3>
            {citations && Object.entries(citations).map(([key, value]) => (
              <div key={key} className={styles.citation}>
                <h5>{key}</h5>
                {value.abstract && value.abstract.map((item, index) => (
                  <p key={index}>
                    <strong>Abstract:</strong> {item.before} <span className={styles.highlight}>{item.highlight}</span> {item.after}
                  </p>
                ))}
                {value.claims && value.claims.map((item, index) => (
                  <p key={index}>
                    <strong>Claim:</strong> {item.before} <span className={styles.highlight}>{item.highlight}</span> {item.after}
                  </p>
                ))}
                {value.description && (
                  <p>
                    <strong>Description:</strong> {value.description}
                  </p>
                )}
              </div>
            ))}
          </div> */}
        </div>
      </div>
      <Footer />
    </>
  );
};

export default Page;
