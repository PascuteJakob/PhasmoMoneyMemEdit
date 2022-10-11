from pymeow import *

offsets = [0xB8, 0x18, 0x20, 0x150, 0xA0, 0x288, 0x18]
game_process = process_by_name('Phasmophobia.exe')
game_module = game_process['modules']['UnityPlayer.dll']['baseaddr']
money_addr = read_int64(game_process, game_module + 0x0179E170)



money_dyna_addr = pointer_chain(game_process, game_module + 0x0179E170, [0xB8, 0x18, 0x20, 0x150, 0xA0, 0x288])


desired_money = input('Input desired money.\n')
desired_money_int = int(desired_money)

write_int64(game_process, money_dyna_addr + 0x18, desired_money_int)
