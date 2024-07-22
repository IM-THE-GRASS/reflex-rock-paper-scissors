import reflex as rx
import random

class GameState(rx.State):
    choices = ["rock", "paper", "scissors"]
    player_choice: str = ""
    computer_choice: str = ""
    result: str = ""
    

    def play(self, player_choice: str):
        self.player_choice = player_choice
        self.computer_choice = random.choice(self.choices)
        self.result = self.get_result()

    def get_result(self):
        if self.player_choice == self.computer_choice:
            return "It's a tie!"
        elif (
            (self.player_choice == "rock" and self.computer_choice == "scissors") or
            (self.player_choice == "paper" and self.computer_choice == "rock") or
            (self.player_choice == "scissors" and self.computer_choice == "paper")
        ):
            return "You win!"
        else:
            return "Computer wins!"

def choice_button(choice: str):
    return rx.button(
        choice.capitalize(),
        on_click=GameState.play(choice),
        size="lg",
        width="100px",
        color_scheme="green"
    )

def index():
    return rx.center(
        rx.card(
            rx.vstack(
                rx.heading("Rock Paper Scissors", size="2xl", margin_bottom="1em", color_scheme="green"),
                rx.hstack(
                    choice_button("rock"),
                    choice_button("paper"),
                    choice_button("scissors"),
                    spacing="4",
                    margin_bottom="2em",
                ),
                rx.hstack(
                    rx.vstack(
                        rx.text("Your choice: ", font_weight="bold", color_scheme="green"),
                        rx.text(GameState.player_choice, font_weight="bold", color_scheme="green"),
                    ),
                    rx.vstack(
                        rx.text("Computer's choice: ", font_weight="bold", color_scheme="green"),
                        rx.text(GameState.computer_choice, font_weight="bold", color_scheme="green"),
                    ),
                    rx.vstack(
                        rx.text("Result: ", font_weight="bold", color_scheme="green"),
                        rx.text(GameState.result, font_weight="bold", color_scheme="green"),
                    )
                ),
                padding="1em",
                border_radius="md",
                width="100%",
            ),
            width="400px",
            spacing="4",
            padding="2em",
            variant="surface",
            border_radius="lg",
            box_shadow="lg",
        ),
        width="100%",
        height="100vh",
    )

app = rx.App(theme=rx.theme(
        appearance="dark",
        has_background=True,
        radius="large",
        accent_color="green",
    )
)
app.add_page(index)
