import dynamic from "next/dynamic";
import React from "react";
import { Center } from "@chakra-ui/react";
import useSWR from "swr";

const Holocron = dynamic(() => import("@sampoder/holocron"), { ssr: false });

const VrPlayer = dynamic(() => import("react-vr-player"), { ssr: false });

function Title() {
  return <h1 style={{ color: "white", fontWeight: '800' }}>The Climatator</h1>;
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
        mode="duo"
        fullscreen={<FullscreenButton />}
      >
        {data.started == 0 ? (
          <p className="vertical-center">
            <h1>The Climatator</h1>
            <p>Please wait for the conductor to begin the experience.</p>
          </p>
        ) : (
          <video
            autoPlay
            className="vertical-center"
            src="https://cloud-km5shtklv.vercel.app/0rangolidemo.mp4"
          />
        )}
      </Holocron>
      <style>{`
        .css-h74a88 { 
          position: relative;
        }

        .css-2umnz{
          position: relative;
        }
        
        .vertical-center {
          padding: 40px;
          margin: 0;
          max-height: 100%;
          position: absolute;
          top: 50%;
          -ms-transform: translateY(-50%);
          transform: translateY(-50%);
          text-align: center;
          color: white;
        }
        .vertical-center > h1 { 
          font-size: 2em;
          font-weight: 800;
        }
        `}</style>
    </div>
  );
}
