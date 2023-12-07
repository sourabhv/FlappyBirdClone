import asyncio
from src.flappyEnv2 import FlappyEnv2
from models.FA.DynaQ import dynaq
from models.featurizer.tile_coding_6d import TileCoder
from src.models.A2Helpers import RbfFeaturizer


async def run():
    env = FlappyEnv2()

    ftr = RbfFeaturizer(env, 100)
    W = await dynaq.DynaQFA(env, ftr, epsilon=0.1, max_episode=100000)
    print(W)
    env.close()

    return
    for episode in range(0):
        await env.reset()
        total_reward = 0
        while True:
            action = env.action_space.sample()
            action = 1 if env.np_random.choice(20) == 0 else 0
            obs, reward, game_over, _, info = await env.step(action)
            total_reward += reward
            # print(obs)
            if game_over:
                print_episode_data(episode+1, total_reward)
                break           
    env.close()

def print_episode_data(episode, total_reward):
    print("--------------")
    print(f"Episode: {episode}")
    print(f"Score: {total_reward}")

if __name__ == "__main__":
    asyncio.run(run())
