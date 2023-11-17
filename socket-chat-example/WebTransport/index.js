import { readFile } from "node:fs/promises";
import { createServer } from "node:https";

const key = await readFile("./key.pem");
const cert = await readFile("./cert.pem");

const httpsServer = createServer({
  key,
  cert
}, async (req, res) => {
  if (req.method === "GET" && req.url === "/") {
    const content = await readFile("./index.html");
    res.writeHead(200, {
      "content-type": "text/html"
    });
    res.write(content);
    res.end();
  } else {
    res.writeHead(404).end();
  }
});

const port = process.env.PORT || 3000;

httpsServer.listen(port, () => {
  console.log(`server listening at https://localhost:${port}`);
});

