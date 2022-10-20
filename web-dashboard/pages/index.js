import dynamic from "next/dynamic";
import React, { useState, useEffect } from "react";
import { Box, Center } from "@chakra-ui/react";
import useSWR from "swr";
import Head from 'next/head'

const Holocron = dynamic(() => import("@sampoder/holocron"), { ssr: false });

const VrPlayer = dynamic(() => import("react-vr-player"), { ssr: false });

function Title() {
  return <h1 style={{ color: "white", fontWeight: "800" }}>The Climatator</h1>;
}

function LaunchButton() {
  return <button style={{ color: "white" }}>Play</button>;
}

function FullscreenButton() {
  return <button style={{ color: "white" }}>Fullscreen</button>;
}

export default function App() {
  const fetcher = (...args) => fetch(...args).then((res) => res.json());
  const { data, error } = useSWR("/api/status", fetcher, {
    refreshInterval: 100,
  });

  if (error) return <div>failed to load</div>;
  if (!data) return <div>loading...</div>;

  console.log(data);
  return (
    <div className="App">
      <Holocron
        title={<Title />}
        backgroundColor="#8492a6"
        launch={<LaunchButton />}
        mode="fullscreen"
        fullscreen={<FullscreenButton />}
      >
        {data.started == 0 ? (
          <p className="vertical-center">
            <h1>The Climatator</h1>
            <p>Please wait for the conductor to begin the experience.</p>
          </p>
        ) : (
          <Box
            bg="black"
            style={{
              padding: "40px",
              paddingRight: "0px",
              paddingLeft: "0px",
              height: "100vh",
            }}
          >
            <iframe width="100%" height="100%" src="/video.html">
            </iframe>
          </Box>
        )}
      </Holocron>
      <style>{`
        
        .vertical-center > h1 { 
          font-size: 2em;
          font-weight: 800;
        }
        `}</style>
    </div>
  );
}
