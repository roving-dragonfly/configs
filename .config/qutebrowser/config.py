### Qutebrowser config

## Bindings
# Unbind needed keys
config.unbind('<Ctrl-x>')
config.unbind('d')
# Reload config
config.bind('<Ctrl-x><Ctrl-r>', 'config-source')
# Emacs edition
c.editor.command = ['edit', '{}']
config.bind('<Ctrl-x><Ctrl-e>', 'open-editor', mode='insert')
# Cancel w/ Esc and C-g
config.bind('<Escape>', 'leave-mode', mode='insert')
config.bind('<Ctrl-g>', 'leave-mode', mode='insert')
config.bind('<Escape>', 'leave-mode', mode='command')
config.bind('<Ctrl-g>', 'leave-mode', mode='command')
# Tabs
config.bind('x', 'tab-close')
config.bind('J', 'tab-prev')
config.bind('K', 'tab-next')
config.bind('r', 'reload')
config.bind('<Ctrl-x>1', 'tab-only')
# Search
config.bind('<Ctrl-s>', 'set-cmd-text /', mode='normal')
config.bind('<Ctrl-r>', 'set-cmd-text ?', mode='normal')
config.bind('<Ctrl-s>', 'search-next', mode='command')
config.bind('<Ctrl-r>', 'search-prev', mode='command')
# Zoom
config.bind('+', 'zoom-in')
config.bind('-', 'zoom-out')
# Command
config.bind('<Alt-x>', 'set-cmd-text :')

## Misc
# Tabs
c.tabs.position = 'left'
c.tabs.width = '30%'
c.tabs.show = 'switching'
c.tabs.show_switching_delay = 1000
c.tabs.select_on_remove = 'last-used'
c.tabs.title.format = '{audio}{title}'
#Dark mode
c.content.user_stylesheets = "./solarized-dark-all-sites.css"


# Smooth scrolling
c.scrolling.smooth = False
# Saves previous session
c.auto_save.session = True

