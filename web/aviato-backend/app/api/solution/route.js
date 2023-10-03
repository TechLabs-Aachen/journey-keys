import { NextResponse } from "next/server";

export async function GET(req) {
  // TODO: simply replace your email here
  return NextResponse.json({email: "youremail@email.com"})
}
