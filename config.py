# Setting for Blocks
# Number of blocks
num_blocks = (5, 3)
# Size of margin
margin = (60, 40)
# Size of block
block_size = (80, 30)
# Spacing between blocks
spacing = (20, 20)
score_pos = (10, 10)
life_pos = (450, 10)

# Display setting
fps = 30
wall_width = 10
scoreboard_height = 50
gameboard_height_coefficient = 3

display_dimension = (600, 800)


center_x = display_dimension[0] / 2
center_y = display_dimension[1] / 2


# Setting for paddle
paddle_color = (242, 242, 0)
paddle_pos = (center_x, display_dimension[1] - 100)
paddle_size = (100, 30)
paddle_speed = 5

# Setting for ball
ball_color = (242, 242, 0)
ball_speed = display_dimension[1] / 80
ball_pos = (center_x, paddle_pos[1] - paddle_size[1])
ball_fever_color = (255, 50, 0)
ball_size = (20, 20)

# Setting for items
item_size = (20, 20)
item_default_color = (255, 255, 255)    # 기본 아이템 색상 (흰색)
item_blue_color = (64, 64, 255) # 파란 아이템 색상 (조금 밝은 파란색)
item_speed = 5
scattering_angle = 30   # 아이템 획득 시 새 공이 좌우로 퍼지는 각도. 공이 45도로 올라가고 있었다면 15도, 75도로 두 개 발사함

fever_time = 5

add_score = 100
add_score_color = (0, 255, 0)

paddle_long_ratio = 2
paddle_long_time = 5
paddle_long_color = (0, 126, 255)

colors = [(255, 0, 0), (255, 165, 0), (255, 255, 0)]
collision_limit = len(colors) - 1

# Total number of life.
life = 3