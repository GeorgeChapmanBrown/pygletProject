def __init__(self, *args, **kwargs):
    super(Player, self).__init__(img=resources.player_image, *args, **kwargs)

    # Create a child sprite to show when the ship is thrusting
    self.engine_sprite = pyglet.sprite.Sprite(img=resources.engine_image, *args, **kwargs)
    self.engine_sprite.visible = False

    # Set some easy-to-tweak constants
    self.thrust = 300.0
    self.rotate_speed = 200.0
    self.bullet_speed = 700.0

    # Player should not collide with own bullets
    self.reacts_to_bullets = False

    # Tell the game handler about any event handlers
    self.key_handler = key.KeyStateHandler()
    self.event_handlers = [self, self.key_handler]