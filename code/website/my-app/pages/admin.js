import dynamic from "next/dynamic";
import React from "react";
import { Box, Center, Heading, Button, Stack } from "@chakra-ui/react";
import useSWR from "swr";

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
      <Center height="100vh" width="100vw" bg="#CBD5E0">
        <Box bg="#F7FAFC" borderRadius="20px" p="24px">
          <Heading>Climatator Admin</Heading>
          <Stack
            direction="row"
            spacing={4}
            margin="auto"
            textAlign="center"
            align="center"
            justifyContent="center"
            mt="12px"
          >
            <Button colorScheme="green" variant="solid" width="40%" onClick={() => fetch('/api/started')}>
              Start
            </Button>
            <Button colorScheme="red" variant="solid" width="40%" onClick={() => fetch('/api/finished')}>
              Stop
            </Button>
          </Stack>
        </Box>
      </Center>
    </div>
  );
}
