#####################################################
#Demo using MaKey MaKey to trigger sounds in Sonic Pi
#written by Claire Quigley, January 2018
#####################################################

# commands to run for each symbol on the MaKey MaKey
# (example just uses symbols on the front of the device)
up = "cue :upcue"
down = "sample :misc_crow"
left = "sample :perc_snap"
right = "sample :misc_cineboom"
space = "use_synth :hoover \n play :c4"
click = "play :g5"

# make an array containing all of the commands
# so that we can refer to them by number
sounds = [up, right, down, left, space, click]

# loop triggered by pressing 'up' symbol
live_loop :uploop do
  sync :upcue
  with_fx :echo do
    sample :bass_trance_c
    sleep 1
    sample :bd_haus
    sleep 0.5
    sample :bd_haus
    sleep 0.5
  end
end


# looks for messages from the MaKey MaKey via Pygame Zero
# and runs appropriate command
live_loop :get_note do
  use_real_time
  set_sched_ahead_time! 0     #removes 'lag' between pressing symbol and sound playing
  n = sync "/osc/play"
  symbol = n[0]
  run_code sounds[pad]
end

