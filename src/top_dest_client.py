from messages import TopDestinations, UAgentResponse
from uagents import Agent, Context
from uagents.setup import fund_agent_if_low
import os
 
TOP_DESTINATIONS_CLIENT_SEED = os.getenv("TOP_DESTINATIONS_CLIENT_SEED", "top_destinations_client really secret phrase :)")
 
top_dest_client = Agent(
    name="top_destinations_client",
    port=8008,
    seed=TOP_DESTINATIONS_CLIENT_SEED,
    endpoint=["http://127.0.0.1:8008/submit"],
)
fund_agent_if_low(top_dest_client.wallet.address())
 
top_dest_request = TopDestinations(preferences="new york")
 
@top_dest_client.on_interval(period=10.0)
async def send_message(ctx: Context):
    await ctx.send("agent1qd2jvf7r3k25x03pcu8920xf7geeeuw3cheqymqejhjj4zcluq8xj9lfld2", top_dest_request)
 
@top_dest_client.on_message(model=UAgentResponse)
async def message_handler(ctx: Context, _: str, msg: UAgentResponse):
    ctx.logger.info(f"Received top destination options from: {msg.options}")
 
if __name__ == "__main__":
    top_dest_client.run()