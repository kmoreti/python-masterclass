import random
try:
    import tkinter
except ImportError:
    import Tkinter as tkinter


def load_images(card_images):
    suits = ["heart", "club", "diamond", "spade"]
    face_cards = ["jack", "queen", "king"]

    if tkinter.TkVersion >= 8.6:
        extension = "png"
    else:
        extension = "ppm"

    # for each suit, retrieve the image for the cards
    for suit in suits:
        # first the number cards 1 to 10
        for card in range(1, 11):
            name = "cards/{}_{}.{}".format(str(card), suit, extension)
            image = tkinter.PhotoImage(file=name)
            card_images.append((card, image,))

        # next the face cards
        for card in face_cards:
            name = "cards/{}_{}.{}".format(str(card), suit, extension)
            image = tkinter.PhotoImage(file=name)
            card_images.append((10, image,))


def _deal_card(frame):
    # pop the next car off the top of the deck
    next_card = deck.pop(0)
    # and add it to back of the pack
    deck.append(next_card)
    # add the image to a Label and display the label
    tkinter.Label(frame, image=next_card[1], relief="raised").pack(side="left")
    return next_card


def deal_dealer():
    dealer_score = score_hand(dealer_hand)
    while 0 < dealer_score < 17:
        dealer_hand.append(_deal_card(dealer_card_frame))
        dealer_score = score_hand(dealer_hand)
        dealer_score_label.set(dealer_score)

    player_score = score_hand(player_hand)
    if player_score > 21:
        result_text.set("Dealer Wins!")
    elif dealer_score > 21 or dealer_score < player_score:
        result_text.set("Player Wins")
    elif dealer_score > player_score:
        result_text.set("Dealer Wins")
    else:
        result_text.set("Draw!")
    dealer_button.configure(state='disabled')
    player_button.configure(state='disabled')
    result.configure(background='purple')


def deal_player():
    player_hand.append(_deal_card(player_card_frame))
    player_score = score_hand(player_hand)
    player_score_label.set(player_score)
    if player_score > 21:
        result_text.set("Dealer Wins!")
        dealer_button.configure(state='disabled')
        player_button.configure(state='disabled')
        result.configure(background='purple')
    # global player_score
    # global player_ace
    # card_value = deal_card(player_card_frame)[0]
    # if card_value == 1 and not player_ace:
    #     player_ace = True
    #     card_value = 11
    # player_score += card_value
    # # if we would bust, check if there is an ace and subtract
    # if player_score > 21 and player_ace:
    #     player_score -= 10
    #     player_ace = False
    # player_score_label.set(player_score)
    # if player_score > 21:
    #     result_text.set("Dealer wins")
    # print(locals())


def score_hand(hand):
    # Calculate the total score of all cards in the list
    # Only one ace can have the value 11, an this will reduce to 1 if the hand would bust
    score = 0
    ace = False
    for next_card in hand:
        card_value = next_card[0]
        if card_value == 1 and not ace:
            ace = True
            card_value = 11
        score += card_value
        # if we would bust, check if there is an ace and subtract 10
        if score > 21 and ace:
            score -= 10
            ace = False
    return score


def initial_deal():
    deal_player()
    dealer_hand.append(_deal_card(dealer_card_frame))
    dealer_score_label.set(score_hand(dealer_hand))
    deal_player()
    result.configure(background='green')


def new_game():
    global dealer_card_frame, player_card_frame, dealer_hand, player_hand

    # embedded frame to hold the card images
    dealer_card_frame.destroy()
    dealer_card_frame = tkinter.Frame(card_frame, background="green")
    dealer_card_frame.grid(row=0, column=1, sticky="ew", rowspan=2)
    player_card_frame.destroy()
    player_card_frame = tkinter.Frame(card_frame, background="green")
    player_card_frame.grid(row=2, column=1, sticky='ew', rowspan=2)
    dealer_button.configure(state='normal')
    player_button.configure(state='normal')

    result_text.set("")

    dealer_hand = []
    player_hand = []
    initial_deal()


def shuffle():
    random.shuffle(deck)


def play():
    initial_deal()
    main_window.mainloop()


main_window = tkinter.Tk()

# Set up the screen and frames for the dealer and player
main_window.title("Black Jack")
main_window.geometry("640x480")
main_window.configure(background="green")

result_text = tkinter.StringVar()
result = tkinter.Label(main_window, textvariable=result_text, width=20, background="green", fg='white')
result.grid(row=0, column=0, columnspan=3)

card_frame = tkinter.Frame(main_window, relief="sunken", borderwidth=1, background="green")
card_frame.grid(row=1, column=0, sticky="ew", columnspan=3, rowspan=2)

dealer_score_label = tkinter.IntVar()
tkinter.Label(card_frame, text="Dealer", background="green", fg="white").grid(row=0, column=0)
tkinter.Label(card_frame, textvariable=dealer_score_label, background="green", fg="white").grid(row=1, column=0)

# Embedded frame to hold the card images
dealer_card_frame = tkinter.Frame(card_frame, background="green")
dealer_card_frame.grid(row=0, column=1, sticky="ew", rowspan=2)

player_score_label = tkinter.IntVar()
tkinter.Label(card_frame, text="Player", background="green", fg="white").grid(row=2, column=0)
tkinter.Label(card_frame, textvariable=player_score_label, background="green", fg="white").grid(row=3, column=0)

# Embedded frame to hold the card images
player_card_frame = tkinter.Frame(card_frame, background="green")
player_card_frame.grid(row=2, column=1, sticky='ew', rowspan=2)

button_frame = tkinter.Frame(main_window)
button_frame.grid(row=3, column=0, columnspan=3, sticky='w')

dealer_button = tkinter.Button(button_frame, text="Dealer", command=deal_dealer, width=8, state='normal')
dealer_button.grid(row=0, column=0)

player_button = tkinter.Button(button_frame, text="Player", command=deal_player, width=8, state='normal')
player_button.grid(row=0, column=1)

new_game_button = tkinter.Button(button_frame, text="New Game", command=new_game, width=8, state='normal')
new_game_button.grid(row=0, column=2)

shuffle_button = tkinter.Button(button_frame, text="Shuffle", command=shuffle, width=8, state='normal')
shuffle_button.grid(row=0, column=3)

# load cards
cards = []
load_images(cards)

# Create the list to store the dealer's and player's hands
dealer_hand = []
player_hand = []

# Create a new deck of cards and shuffle them
deck = list(cards)

shuffle()

if __name__ == "__main__":
    play()
