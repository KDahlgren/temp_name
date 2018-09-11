#!/usr/bin/env python

'''
geli.py
'''

# std modules
import string

# custom modules
#

class Gel( object ) :
  '''Contains the gel interface code.

  ATTRIBUTES
  ----------

  METHODS
  -------

  '''

  #################
  #  CONSTRUCTOR  #
  #################
  def __init__( self ) :
    return


  ################
  #  TO RUNBOOK  #
  ################
  def to_runbook( self, spec_serialization_lines ) :
    '''Use serialized spec lines to create a runbook
       for building the system.

    PARAMETERS
    ----------
    spec_serialization_lines : list, required
      The serialized lines of the tranlsated Gel spec.

    RETURN
    ------
    runbook : list
      The sequence of commands required to build the system.

    '''

    tool_list = []
    for line in spec_serialization_lines :
      tools = line.translate( None, string.whitespace ).split( "<-" )[1]
      tools = tools.split( "," )
      tools = [ x.split( "(" )[0] for x in tools ]
      tool_list.extend( tools )

    # define runbook
    runbook = []
    for tool in tool_list :
      runbook.append( "python piper.py install " + tool )

    return runbook


#########################
#  THREAD OF EXECUTION  #
#########################
if __name__ == "__main__" :
  g = Gel()

  # sqlite3  with ontods
  # pickledb with aggs and conman
  # mongodb  with quest and yprov
  spec = [ "sys(X) <- ontods(X),sqlite3(X);", \
           "sys(X) <- aggspack(X),conman(X),pickledb(X);", \
           "sys(X) <- quest(X),yprov(X),sqlite3(X);" ]

  runbook = g.to_runbook( spec )
  print runbook


#########
#  EOF  #
#########
