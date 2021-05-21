config.load_autoconfig(False)

config.set('content.cookies.accept', 'all', 'chrome-devtools://*')
config.set('content.cookies.accept', 'all', 'devtools://*')

config.set('content.headers.accept_language', '', 'https://matchmaker.krunker.io/*')
config.set('content.headers.user_agent', 'Mozilla/5.0 ({os_info}) AppleWebKit/{webkit_version} (KHTML, like Gecko) {upstream_browser_key}/{upstream_browser_version} Safari/{webkit_version}', 'https://web.whatsapp.com/')
config.set('content.headers.user_agent', 'Mozilla/5.0 ({os_info}; rv:71.0) Gecko/20100101 Firefox/71.0', 'https://accounts.google.com/*')
config.set('content.headers.user_agent', 'Mozilla/5.0 ({os_info}) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/99 Safari/537.36', 'https://*.slack.com/*')
config.set('content.headers.user_agent', 'Mozilla/5.0 ({os_info}; rv:71.0) Gecko/20100101 Firefox/71.0', 'https://docs.google.com/*')
config.set('content.headers.user_agent', 'Mozilla/5.0 ({os_info}; rv:71.0) Gecko/20100101 Firefox/71.0', 'https://drive.google.com/*')

config.set('content.images', True, 'chrome-devtools://*')
config.set('content.images', True, 'devtools://*')

config.set('content.javascript.enabled', True, 'chrome-devtools://*')
config.set('content.javascript.enabled', True, 'devtools://*')
config.set('content.javascript.enabled', True, 'chrome://*/*')
config.set('content.javascript.enabled', True, 'qute://*/*')

config.set('content.notifications.enabled', False, 'https://www.youtube.com')

#config.set("colors.webpage.darkmode.enabled", True)

c.downloads.location.directory = '/home/ton1czech/Downloads'

c.aliases = {'q': 'quit', 'w': 'session-save', 'wq': 'quit --save'}

c.url.searchengines = {'DEFAULT': 'https://duckduckgo.com/?q={}', 
                       'aw': 'https://wiki.archlinux.org/?search={}',
                       'wp': 'https://wikipedia.com/wiki/{}',
                       'rd': 'https://reddit.com/search/?q={}'}

config.bind(',ap', 'config-cycle content.user_stylesheets ~/Documents/solarized-everything-css/css/apprentice/apprentice-all-sites.css ""')
config.bind(',dc', 'config-cycle content.user_stylesheets ~/Documents/solarized-everything-css/css/darculized/darculized-all-sites.css ""')
config.bind(',gr', 'config-cycle content.user_stylesheets ~/Documents/solarized-everything-css/css/gruvbox/gruvbox-all-sites.css ""')
config.bind(',sd', 'config-cycle content.user_stylesheets ~/Documents/solarized-everything-css/css/solarized-dark/solarized-dark-all-sites.css ""')
config.bind(',sl', 'config-cycle content.user_stylesheets ~/Documents/solarized-everything-css/css/solarized-light/solarized-light-all-sites.css ""')

def blood(c, options = {}):
    palette = {
        'background': '#282a36',
        'background-alt': '#282a36', 
        'background-attention': '#181920',
        'border': '#282a36',
        'current-line': '#44475a',
        'selection': '#44475a',
        'foreground': '#f8f8f2',
        'foreground-alt': '#e0e0e0',
        'foreground-attention': '#ffffff',
        'comment': '#6272a4',
        'cyan': '#8be9fd',
        'green': '#50fa7b',
        'orange': '#ffb86c',
        'pink': '#ff79c6',
        'purple': '#bd93f9',
        'red': '#ff5555',
        'yellow': '#f1fa8c'
    }   

    spacing = options.get('spacing', {
        'vertical': 5,
        'horizontal': 5
    })

    padding = options.get('padding', {
        'top': spacing['vertical'],
        'right': spacing['horizontal'],
        'bottom': spacing['vertical'],
        'left': spacing['horizontal']
    })

    c.colors.completion.category.bg = palette['background']
    c.colors.completion.category.border.bottom = palette['border']
    c.colors.completion.category.border.top = palette['border']
    c.colors.completion.category.fg = palette['foreground']
    c.colors.completion.even.bg = palette['background']
    c.colors.completion.odd.bg = palette['background-alt']
    c.colors.completion.fg = palette['foreground']
    c.colors.completion.item.selected.bg = palette['selection']
    c.colors.completion.item.selected.border.bottom = palette['selection']
    c.colors.completion.item.selected.border.top = palette['selection']
    c.colors.completion.item.selected.fg = palette['foreground']
    c.colors.completion.match.fg = palette['orange']
    c.colors.completion.scrollbar.bg = palette['background']
    c.colors.completion.scrollbar.fg = palette['foreground']

    c.colors.downloads.bar.bg = palette['background']
    c.colors.downloads.error.bg = palette['background']
    c.colors.downloads.error.fg = palette['red']
    c.colors.downloads.stop.bg = palette['background']
    c.colors.downloads.system.bg = 'none'

    c.colors.hints.bg = palette['background']
    c.colors.hints.fg = palette['purple']

    c.hints.border = '1px solid ' + palette['background-alt']

    c.colors.hints.match.fg = palette['foreground-alt']

    c.colors.keyhint.bg = palette['background']
    c.colors.keyhint.fg = palette['purple']
    c.colors.keyhint.suffix.fg = palette['selection']

    c.colors.messages.error.bg = palette['background']
    c.colors.messages.error.border = palette['background-alt']
    c.colors.messages.error.fg = palette['red']
    c.colors.messages.info.bg = palette['background']
    c.colors.messages.info.border = palette['background-alt']
    c.colors.messages.info.fg = palette['comment']
    c.colors.messages.warning.bg = palette['background']
    c.colors.messages.warning.border = palette['background-alt']
    c.colors.messages.warning.fg = palette['red']

    c.colors.prompts.bg = palette['background']
    c.colors.prompts.border = '1px solid ' + palette['background-alt']
    c.colors.prompts.fg = palette['cyan']
    c.colors.prompts.selected.bg = palette['selection']

    c.colors.statusbar.caret.bg = palette['background']
    c.colors.statusbar.caret.fg = palette['orange']
    c.colors.statusbar.caret.selection.bg = palette['background']
    c.colors.statusbar.caret.selection.fg = palette['orange']
    c.colors.statusbar.command.bg = palette['background']
    c.colors.statusbar.command.fg = palette['pink']
    c.colors.statusbar.command.private.bg = palette['background']
    c.colors.statusbar.command.private.fg = palette['foreground-alt']
    c.colors.statusbar.insert.bg = palette['background-attention']
    c.colors.statusbar.insert.fg = palette['foreground-attention']
    c.colors.statusbar.normal.bg = palette['background']
    c.colors.statusbar.normal.fg = palette['foreground']
    c.colors.statusbar.passthrough.bg = palette['background']
    c.colors.statusbar.passthrough.fg = palette['orange']
    c.colors.statusbar.private.bg = palette['background-alt']
    c.colors.statusbar.private.fg = palette['foreground-alt']
    c.colors.statusbar.progress.bg = palette['background']
    c.colors.statusbar.url.error.fg = palette['red']
    c.colors.statusbar.url.fg = palette['foreground']
    c.colors.statusbar.url.hover.fg = palette['cyan']
    c.colors.statusbar.url.success.http.fg = palette['green']
    c.colors.statusbar.url.success.https.fg = palette['green']
    c.colors.statusbar.url.warn.fg = palette['yellow']

    c.statusbar.padding = padding

    c.colors.tabs.bar.bg = palette['selection']
    c.colors.tabs.even.bg = palette['selection']
    c.colors.tabs.even.fg = palette['foreground']
    c.colors.tabs.indicator.error = palette['red']
    c.colors.tabs.indicator.start = palette['orange']
    c.colors.tabs.indicator.stop = palette['green']
    c.colors.tabs.indicator.system = 'none'
    c.colors.tabs.odd.bg = palette['selection']
    c.colors.tabs.odd.fg = palette['foreground']
    c.colors.tabs.selected.even.bg = palette['background']
    c.colors.tabs.selected.even.fg = palette['foreground']
    c.colors.tabs.selected.odd.bg = palette['background']
    c.colors.tabs.selected.odd.fg = palette['foreground']

    c.tabs.padding = padding
    c.tabs.indicator.width = 1
    c.tabs.favicons.scale = 1


