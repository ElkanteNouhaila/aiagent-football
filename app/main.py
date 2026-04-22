from app.agent import FootballAgent


def main():
    agent = FootballAgent()
    print("Football Agent started. Type 'exit' to quit.\n")

    while True:
        user_input = input("You: ").strip()

        if user_input.lower() == "exit":
            print("Bye.")
            break

        try:
            answer = agent.run(user_input)
            print(f"\nAgent: {answer}\n")
        except Exception as e:
            print(f"\nError: {e}\n")


if __name__ == "__main__":
    main()