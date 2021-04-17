const fetch = require('node-fetch')

module.exports = {
	async redirects() {
		const urls = await fetch(process.env.apiURL).then((x) => x.json())

		const redirects = urls.map((x) => ({
			permanent: true,
			source: `/${x.name}/:wildcards*`,
			destination: `${x.url}/:wildcards*`,
		}))

		if (process.env.baseUrl) {
			redirects.push({
				permanent: true,
				source: '/',
				destination: `${process.env.baseUrl}`,
			})
		}

		console.log(redirects)

		return redirects
	},
	async rewrites() {
		const rewrites = []

		if (!process.env.baseUrl) {
			rewrites.push({
				source: '/',
				destination: '/list',
			})
		}


		rewrites.push({
			source: `/video`,
			destination: 'https://cloud-9uo1pruir-hack-club-bot.vercel.app/0sam_poder_personal_projectt.mov/',
		)}

		return rewrites
	},
	github: {
		autoAlias: true,
		enabled: true,
	},
	trailingSlash: false,
	public: true,
}
