HAVE_CONST = ['LOAD_CONST']
HAVE_NAME = ['LOAD_NAME',
             'STORE_NAME']
HAVE_LABEL = ['JUMP_ABSOLUTE',
              'POP_JUMP_IF_TRUE',
              'POP_JUMP_IF_FALSE',
              'SETUP_LOOP']
HAVE_ARGUMENT = HAVE_LABEL + HAVE_NAME + HAVE_CONST + ['COMPARE_OP']