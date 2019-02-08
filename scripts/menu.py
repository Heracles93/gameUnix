# made with figlet
print("                            _   _       _      ")
print("  __ _  __ _ _ __ ___   ___| | | |_ __ (_)_  __")
print(" / _` |/ _` | '_ ` _ \ / _ \ | | | '_ \| \ \/ /")
print("| (_| | (_| | | | | | |  __/ |_| | | | | |>  < ")
print(" \__, |\__,_|_| |_| |_|\___|\___/|_| |_|_/_/\_\ ")
print(" |___/   ")

print("Press Enter to start the minesweeper")
game = None
while game not in [1,2,3]:
    game = int(input("Enter '1' to start the minesweeper & '2' to start tictactoe & '3' to start blackjack"))

if game == 1:
    import minesweeper
    minesweeper.playgame()
elif game == 2:
    import tictactoe
    tictactoe.playgame()
elif game == 3:
    import blackjack
    blackjack.main()
    