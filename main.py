basic.show_string("Mossie")
music.play(music.tone_playable(262, music.beat(BeatFraction.WHOLE)),
    music.PlaybackMode.UNTIL_DONE)

def on_forever():
    basic.show_arrow(ArrowNames.NORTH)
    basic.pause(2000)
    basic.show_arrow(ArrowNames.EAST)
    basic.pause(2000)
    basic.show_arrow(ArrowNames.SOUTH)
    basic.pause(2000)
    basic.show_arrow(ArrowNames.WEST)
    basic.pause(2000)
basic.forever(on_forever)
