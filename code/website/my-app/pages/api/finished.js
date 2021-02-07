// Next.js API route support: https://nextjs.org/docs/api-routes/introduction

const S1 = require('s1db')
const db = new S1(process.env.S1_TOKEN)

export default async (req, res) => {
  await db.set('started', 0)
  await db.set('video', 0)
  res.statusCode = 200
  res.send('Finished.')
}
