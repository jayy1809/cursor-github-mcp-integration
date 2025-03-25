# Setup GitHub MCP in Cursor

This guide explains how to set up and use the GitHub MCP integration in Cursor.

## Step-by-Step Setup Instructions

### 1. Create a GitHub Personal Access Token (Fine-grained)

1. Go to your GitHub account settings
2. Navigate to Developer Settings > Personal Access Tokens > Fine-grained tokens
3. Click "Generate new token"
4. Give your token a descriptive name
5. Set an expiration date
6. Select the repositories you want to grant access to
7. Configure permissions (recommended to give only the minimum necessary permissions)
8. Click "Generate token"
9. Copy your token (you'll need it in step 2)

### 2. Set Up Smithery.ai GitHub MCP

1. Go to [Smithery.ai](https://smithery.ai)
2. Log in with your GitHub account
3. Navigate to their GitHub MCP server section
4. During installation, look for the Cursor tab
5. Paste your GitHub Personal Access Token from step 1
6. The site will generate a command - copy this command

### 3. Configure Cursor

1. Open Cursor
2. Go to Settings (gear icon)
3. Navigate to the MCP section
4. Click "+ Add new global MCP server"
5. This will create or open an `mcp.json` file
6. In the command field, paste:
   ```
   {
     "mcpServers": {
       "Github": {
         "command": <PASTE YOUR COMMAND>
       }
     }
   }

   (Replace with the command you copied from Smithery.ai)

## Using GitHub MCP in Cursor

Once configured, you can use the Cursor Agent tab to:
- Create new repositories
- Make changes to existing repositories
- Push code directly from Cursor with the help of cursor Agent
- And more!

## Important Notes

- Always use fine-grained tokens with the minimum permissions necessary
- Regularly rotate your access tokens for security
- Check Smithery.ai documentation for the latest features and commands
