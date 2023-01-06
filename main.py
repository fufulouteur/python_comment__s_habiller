temperature = int(input('il fait combien dehors ? '))
if temperature >= 25:
    habit = 'un short et des lunette de soleil.'

elif temperature >= 15 and temperature <= 24:
    habit = 'une veste legere.'

else:
    habit = 'un manteau et une echarpe.'

conseil = (f"aujourd'hui, tu peux mettre {habit}.")
print(conseil)