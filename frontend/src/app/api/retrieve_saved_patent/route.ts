import { NextRequest, NextResponse } from "next/server";
import { backendUrl } from "@/types/types";
import { withApiAuthRequired, getAccessToken } from "@auth0/nextjs-auth0";

export const POST = withApiAuthRequired(async function POST(
    request: NextRequest
) {
    try {
        const body = await request.json();
        // Get the access token
        const { accessToken } = await getAccessToken({
            scopes: ["user"],
        });
        console.log("BODY: ", body);
        const searchURL = new URL(`${backendUrl}/save/fetch_patents`);
        const savePatentResponse = await fetch(searchURL.toString(), {
            method: "POST",
            headers: {
                "Content-Type": "application/json",
                Authorization: `Bearer ${accessToken}`,
            },
            body: JSON.stringify(body),
        });

        if (!savePatentResponse.ok) {
            throw new Error(`HTTP error! :( status: ${savePatentResponse.status}`);
        }

        const response = await savePatentResponse.json();
        return NextResponse.json(response);
    } catch (error) {
        return NextResponse.json({ error: error }, { status: 500 });
    }
});
