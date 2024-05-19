import nextJest from 'next/jest.js'

const createJestConfig = nextJest({dir: "./"})

export default createJestConfig({testEnvironment: "node"})
