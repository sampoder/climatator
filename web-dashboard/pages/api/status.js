// Next.js API route support: https://nextjs.org/docs/api-routes/introduction

const S1 = require('s1db')
const db = new S1(process.env.S1_TOKEN)

export default async (req, res) => {
  res.statusCode = 200
  res.json({started: await db.get('started'), video: await db.get('video')})
}
