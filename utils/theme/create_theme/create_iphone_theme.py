import os

from utils.wallpaper import CreateWallpaper
from utils.theme_preview import CreateIphonePreview
from .color_name import ColorName
from .color_brightness import ColorBrightness


class CreateIphoneTheme(ColorName,
                        ColorBrightness,
                        CreateWallpaper,
                        CreateIphonePreview):
    
    async def _status_bar_gamma(self, hex_color, threshold = 128):
        hex_color = hex_color.lstrip('#')
        rgb = tuple(int(hex_color[i:i+2], 16) for i in (0, 2, 4))
        brightness = sum(rgb) / 3
        
        if brightness < threshold:
            dark = 'true'
            status_bar = 'black'
        else:
            dark = 'false'
            status_bar = 'white'
        
        return dark, status_bar
    
    
    async def create_iphone_theme(self, data, bot_name):
        chat_id = data.get('chat_id')
        image_path = data.get('wallpaper_path')
        bg = data.get('bg_color')
        primary_txt = data.get('primary_color')
        not_primary_txt = data.get('secondary_color')
        dark, status_bar = await self._status_bar_gamma(bg)
        
        color_name: str = await self.hex_to_color_name(bg)
        color_name = color_name.capitalize()
        

        hex_bg = bg
        hex_primary_txt = primary_txt
        hex_not_primary_txt = not_primary_txt
        

        hex_darker_bg = await self._adjust_color_brightness(bg)
        darker_bg =hex_darker_bg[1:]
        hex_secondary_txt = await self._adjust_color_brightness(primary_txt)
        secondary_txt = hex_secondary_txt[1:]
        bg = bg[1:]
        primary_txt = primary_txt[1:]
        not_primary_txt = not_primary_txt[1:]
        
        keyboard = 'light'
        if status_bar == 'light':
            keyboard = 'black'

        wallpaper = await self.get_wallpaper(image_path)

        wallpaper_slug = wallpaper.slug
        name = f'{color_name}_theme_by-{bot_name}'
        file_name = f'{color_name}_theme_by-{bot_name}.tgios-theme'

        theme = os.path.join('src', 'users_data', str(chat_id), file_name)
        
        ios_data = [
            f"",
            f"name: {name}",
            f"basedOn: day",
            f"dark: {dark}",
            f"intro:",
            f"statusBar: {status_bar}",
            f"primaryText: {primary_txt}",
            f"accentText: {not_primary_txt}",
            f"disabledText: 33{secondary_txt}",
            f"startButton: {not_primary_txt}",
            f"dot: {primary_txt}",
            f"passcode:",
            f"  bg:",
            f"    top: {darker_bg}",
            f"    bottom: {darker_bg}",
            f"  button: clear",
            f"root:",
            f"  statusBar: {status_bar}",
            f"  tabBar:",
            f"    background: {darker_bg}",
            f"    separator: 33{not_primary_txt}",
            f"    icon: a1{not_primary_txt}",
            f"    selectedIcon: {not_primary_txt}",
            f"    text: a1{not_primary_txt}",
            f"    selectedText: {not_primary_txt}",
            f"    badgeBackground: {primary_txt}",
            f"    badgeStroke: {darker_bg}",
            f"    badgeText: {darker_bg}",
            f"  navBar:",
            f"    button: {not_primary_txt}",
            f"    disabledButton: 33{not_primary_txt}",
            f"    primaryText: {primary_txt}",
            f"    secondaryText: {not_primary_txt}",
            f"    control: {not_primary_txt}",
            f"    accentText: {not_primary_txt}",
            f"    background: {darker_bg}",
            f"    separator: 33{not_primary_txt}",
            f"    badgeFill: {primary_txt}",
            f"    badgeStroke: {darker_bg}",
            f"    badgeText: {primary_txt}",
            f"  searchBar:",
            f"    background: {darker_bg}",
            f"    accent: {not_primary_txt}",
            f"    inputFill: 33{bg}",
            f"    inputText: {primary_txt}",
            f"    inputPlaceholderText: a1{not_primary_txt}",
            f"    inputIcon: 33{darker_bg}",
            f"    inputClearButton: {darker_bg}",
            f"    separator: 33{not_primary_txt}",
            f"  keyboard: {keyboard}",
            f"list:",
            f"  blocksBg: {darker_bg}",
            f"  plainBg: {darker_bg}",
            f"  primaryText: {primary_txt}",
            f"  secondaryText: {not_primary_txt}",
            f"  disabledText: 1e{not_primary_txt}",
            f"  accent: {not_primary_txt}",
            f"  highlighted: 1e{not_primary_txt}",
            f"  destructive: ff3b30",
            f"  placeholderText: {not_primary_txt}",
            f"  itemBlocksBg: {darker_bg}",
            f"  itemHighlightedBg: 1e{not_primary_txt}",
            f"  blocksSeparator: 33{not_primary_txt}",
            f"  plainSeparator: 33{not_primary_txt}",
            f"  disclosureArrow: {secondary_txt}",
            f"  sectionHeaderText: {primary_txt}",
            f"  freeText: {primary_txt}",
            f"  freeTextError: cf3030",
            f"  freeTextSuccess: 26972c",
            f"  freeMonoIcon: {darker_bg}",
            f"  switch:",
            f"    frame: e0e0e0",
            f"    handle: ffffff",
            f"    content: 77d572",
            f"    positive: 00c900",
            f"    negative: ff3b30",
            f"  disclosureActions:",
            f"    neutral1:",
            f"      bg: {not_primary_txt}",
            f"      fg: {primary_txt}",
            f"    neutral2:",
            f"      bg: {not_primary_txt}",
            f"      fg: {primary_txt}",
            f"    destructive:",
            f"      bg: {not_primary_txt}",
            f"      fg: {primary_txt}",
            f"    constructive:",
            f"      bg: {not_primary_txt}",
            f"      fg: {primary_txt}",
            f"    accent:",
            f"      bg: {not_primary_txt}",
            f"      fg: {primary_txt}",
            f"    warning:",
            f"      bg: {not_primary_txt}",
            f"      fg: {primary_txt}",
            f"    inactive:",
            f"      bg: {not_primary_txt}",
            f"      fg: {primary_txt}",
            f"  check:",
            f"    bg: {not_primary_txt}",
            f"    stroke: c7c7cc",
            f"    fg: {primary_txt}",
            f"  controlSecondary: {secondary_txt}",
            f"  freeInputField:",
            f"    bg: {darker_bg}",
            f"    stroke: {darker_bg}",
            f"    placeholder: {not_primary_txt}",
            f"    primary: {primary_txt}",
            f"    control: {not_primary_txt}",

            f"  mediaPlaceholder: {not_primary_txt}",
            f"  scrollIndicator: 4c{darker_bg}",
            f"  pageIndicatorInactive: {secondary_txt}",
            f"  inputClearButton: {darker_bg}",
            f"chatList:",
            f"  bg: {bg}",
            f"  itemSeparator: 33{not_primary_txt}",
            f"  itemBg: 1e{darker_bg}",
            f"  pinnedItemBg: {darker_bg}",
            f"  itemHighlightedBg: 1e{not_primary_txt}",
            f"  itemSelectedBg: 1e{not_primary_txt}",
            f"  title: {primary_txt}",
            f"  secretTitle: {primary_txt}",
            f"  dateText: {not_primary_txt}",
            f"  authorName: {secondary_txt}",
            f"  messageText: {not_primary_txt}",
            f"  messageDraftText: {not_primary_txt}",
            f"  checkmark: {not_primary_txt}",
            f"  pendingIndicator: {not_primary_txt}",
            f"  failedFill: ff3b30",
            f"  failedFg: ffffff",
            f"  muteIcon: {not_primary_txt}",
            f"  unreadBadgeActiveBg: {not_primary_txt}",
            f"  unreadBadgeActiveText: {not_primary_txt}",
            f"  unreadBadgeInactiveBg: {secondary_txt}",
            f"  unreadBadgeInactiveText: {not_primary_txt}",
            f"  pinnedBadge: {not_primary_txt}",
            f"  pinnedSearchBar: {bg}",
            f"  regularSearchBar: {bg}",
            f"  sectionHeaderBg: 33{bg}",
            f"  sectionHeaderText: {primary_txt}",
            f"  verifiedIconBg: {darker_bg}",
            f"  verifiedIconFg: {secondary_txt}",
            f"  secretIcon: {darker_bg}",
            f"  pinnedArchiveAvatar:",
            f"    background:",
            f"      top: 1e{not_primary_txt}",
            f"      bottom: {not_primary_txt}",
            f"    foreground: {secondary_txt}",
            f"  unpinnedArchiveAvatar:",
            f"    background:",
            f"      top: 1e{secondary_txt}",
            f"      bottom: {secondary_txt}",
            f"    foreground: {not_primary_txt}",
            f"  onlineDot: {primary_txt}",
            f"chat:",
            f"  defaultWallpaper: {wallpaper_slug}",
            f"  message:",
            f"    incoming:",
            f"      bubble:",
            f"        withWp:",
            f"          bg: {darker_bg}",
            f"          highlightedBg: cc{bg}",
            f"          stroke: {darker_bg}",
            f"        withoutWp:",
            f"          bg: {darker_bg}",
            f"          highlightedBg: cc{bg}",
            f"          stroke: {darker_bg}",
            f"      primaryText: {primary_txt}",
            f"      secondaryText: {not_primary_txt}",
            f"      linkText: {not_primary_txt}",
            f"      linkHighlight: 1e{not_primary_txt}",
            f"      scam: ff3b30",
            f"      textHighlight: 1e{not_primary_txt}",
            f"      accentText: {not_primary_txt}",
            f"      accentControl: {not_primary_txt}",
            f"      mediaActiveControl: {not_primary_txt}",
            f"      mediaInactiveControl: {not_primary_txt}",
            f"      pendingActivity: 99{bg}",
            f"      fileTitle: {primary_txt}",
            f"      fileDescription: {primary_txt}",
            f"      fileDuration: 99{secondary_txt}",
            f"      mediaPlaceholder: {not_primary_txt}",
            f"      polls:",
            f"        radioButton: {darker_bg}",
            f"        radioProgress: {not_primary_txt}",
            f"        highlight: 1e{not_primary_txt}",
            f"        separator: {darker_bg}",
            f"        bar: {not_primary_txt}",
            f"      actionButtonsBg:",
            f"        withWp: 66{bg}",
            f"        withoutWp: cc{bg}",
            f"      actionButtonsStroke:",
            f"        withWp: clear",
            f"        withoutWp: {not_primary_txt}",
            f"      actionButtonsText:",
            f"        withWp: {not_primary_txt}",
            f"        withoutWp: {not_primary_txt}",
            f"      textSelection: 4c{not_primary_txt}",
            f"      textSelectionKnob: {not_primary_txt}",
            f"    outgoing:",
            f"      bubble:",
            f"        withWp:",
            f"          bg: {bg}",
            f"          highlightedBg: cc{darker_bg}",
            f"          stroke: {bg}",
            f"        withoutWp:",
            f"          bg: {bg}",
            f"          highlightedBg: cc{darker_bg}",
            f"          stroke: {bg}",
            f"      primaryText: {primary_txt}",
            f"      secondaryText: a5{not_primary_txt}",
            f"      linkText: {primary_txt}",
            f"      linkHighlight: 4c{not_primary_txt}",
            f"      scam: ffffff",
            f"      textHighlight: 4c{primary_txt}",
            f"      accentText: {not_primary_txt}",
            f"      accentControl: {secondary_txt}",
            f"      mediaActiveControl: {secondary_txt}",
            f"      mediaInactiveControl: a5{secondary_txt}",
            f"      pendingActivity: a5{bg}",
            f"      fileTitle: {primary_txt}",
            f"      fileDescription: a5{not_primary_txt}",
            f"      fileDuration: a5{secondary_txt}",
            f"      mediaPlaceholder: {not_primary_txt}",
            f"      polls:",
            f"        radioButton: a5{darker_bg}",
            f"        radioProgress: {darker_bg}",
            f"        highlight: 1e{darker_bg}",
            f"        separator: a5{darker_bg}",
            f"        bar: {bg}",
            f"      actionButtonsBg:",
            f"        withWp: 66{darker_bg}",
            f"        withoutWp: cc{darker_bg}",
            f"      actionButtonsStroke:",
            f"        withWp: clear",
            f"        withoutWp: {not_primary_txt}",
            f"      actionButtonsText:",
            f"        withWp: {not_primary_txt}",
            f"        withoutWp: {not_primary_txt}",
            f"      textSelection: 33{primary_txt}",
            f"      textSelectionKnob: {primary_txt}",
            f"    freeform:",
            f"      withWp:",
            f"        bg: {bg}",
            f"        highlightedBg: {darker_bg}",
            f"        stroke: {primary_txt}",
            f"      withoutWp:",
            f"        bg: {bg}",
            f"        highlightedBg: {darker_bg}",
            f"        stroke: {primary_txt}",
            f"    infoPrimaryText: {primary_txt}",
            f"    infoLinkText: {primary_txt}",
            f"    outgoingCheck: {not_primary_txt}",
            f"    mediaDateAndStatusBg: 7f{bg}",
            f"    mediaDateAndStatusText: {not_primary_txt}",
            f"    shareButtonBg:",
            f"      withWp: 66{darker_bg}",
            f"      withoutWp: cc{darker_bg}",
            f"    shareButtonStroke:",
            f"      withWp: clear",
            f"      withoutWp: {darker_bg}",
            f"    shareButtonFg:",
            f"      withWp: {darker_bg}",
            f"      withoutWp: {not_primary_txt}",
            f"    mediaOverlayControl:",
            f"      bg: 99{not_primary_txt}",
            f"      fg: {secondary_txt}",
            f"    selectionControl:",
            f"      bg: {not_primary_txt}",
            f"      stroke: {primary_txt}",
            f"      fg: {secondary_txt}",
            f"    deliveryFailed:",
            f"      bg: {not_primary_txt}",
            f"      fg: {secondary_txt}",
            f"    mediaHighlightOverlay: 99{darker_bg}",
            f"  serviceMessage:",
            f"    components:",
            f"      withDefaultWp:",
            f"        bg: cc{bg}",
            f"        primaryText: {primary_txt}",
            f"        linkHighlight: 3f{not_primary_txt}",
            f"        scam: ff3b30",
            f"        dateFillStatic: cc{not_primary_txt}",
            f"        dateFillFloat: cc{not_primary_txt}",
            f"      withCustomWp:",
            f"        bg: 66{bg}",
            f"        primaryText: {primary_txt}",
            f"        linkHighlight: 3f{not_primary_txt}",
            f"        scam: ff3b30",
            f"        dateFillStatic: 66{not_primary_txt}",
            f"        dateFillFloat: 44{not_primary_txt}",
            f"    unreadBarBg: {darker_bg}",
            f"    unreadBarStroke: {darker_bg}",
            f"    unreadBarText: {not_primary_txt}",
            f"    dateText:",
            f"      withWp: {not_primary_txt}",
            f"      withoutWp: {not_primary_txt}",
            f"  inputPanel:",
            f"    panelBg: {darker_bg}",
            f"    panelSeparator: 33{not_primary_txt}",
            f"    panelControlAccent: {not_primary_txt}",
            f"    panelControl: {secondary_txt}",
            f"    panelControlDisabled: 1e{secondary_txt}",
            f"    panelControlDestructive: ff3b30",
            f"    inputBg: 1e{bg}",
            f"    inputStroke: {darker_bg}",
            f"    inputPlaceholder: 33{not_primary_txt}",
            f"    inputText: {primary_txt}",
            f"    inputControl: {not_primary_txt}",
            f"    actionControlBg: {not_primary_txt}",
            f"    actionControlFg: {primary_txt}",
            f"    primaryText: {primary_txt}",
            f"    secondaryText: {not_primary_txt}",
            f"    mediaRecordDot: {not_primary_txt}",
            f"    mediaRecordControl:",
            f"      button: {not_primary_txt}",
            f"      micLevel: 1e{not_primary_txt}",
            f"      activeIcon: {darker_bg}",
            f"  inputMediaPanel:",
            f"    panelSeparator: {darker_bg}",
            f"    panelIcon: {bg}",
            f"    panelHighlightedIconBg: 33{bg}",
            f"    stickersBg: {bg}",
            f"    stickersSectionText: {primary_txt}",
            f"    stickersSearchBg: {bg}",
            f"    stickersSearchPlaceholder: {not_primary_txt}",
            f"    stickersSearchPrimary: {primary_txt}",
            f"    stickersSearchControl: {primary_txt}",
            f"    gifsBg: {bg}",
            f"  inputButtonPanel:",
            f"    panelBg: {bg}",
            f"    panelSeparator: {darker_bg}",
            f"    buttonBg: {darker_bg}",
            f"    buttonStroke: {primary_txt}",
            f"    buttonHighlightedBg: {darker_bg}",
            f"    buttonHighlightedStroke: {primary_txt}",
            f"    buttonText: {primary_txt}",
            f"  historyNav:",
            f"    bg: {darker_bg}",
            f"    stroke: {darker_bg}",
            f"    fg: {primary_txt}",
            f"    badgeBg: {not_primary_txt}",
            f"    badgeStroke: {not_primary_txt}",
            f"    badgeText: {primary_txt}",
            f"actionSheet:",
            f"  dim: 66{darker_bg}",
            f"  bgType: {dark}",
            f"  opaqueItemBg: {bg}",
            f"  itemBg: dd{bg}",
            f"  opaqueItemHighlightedBg: {darker_bg}",
            f"  itemHighlightedBg: b2{darker_bg}",
            f"  opaqueItemSeparator: {darker_bg}",
            f"  standardActionText: {not_primary_txt}",
            f"  destructiveActionText: {not_primary_txt}",
            f"  disabledActionText: {not_primary_txt}",
            f"  primaryText: {primary_txt}",
            f"  secondaryText: {not_primary_txt}",
            f"  controlAccent: {not_primary_txt}",
            f"  inputBg: {bg}",
            f"  inputHollowBg: {bg}",
            f"  inputBorder: {darker_bg}",
            f"  inputPlaceholder: {not_primary_txt}",
            f"  inputText: {primary_txt}",
            f"  inputClearButton: {darker_bg}",
            f"  checkContent: {bg}",
            f"contextMenu:",
            f"  dim: 33{darker_bg}",
            f"  background: c6{bg}",
            f"  itemSeparator: 33{darker_bg}",
            f"  sectionSeparator: 33{darker_bg}",
            f"  itemBg: 00{bg}",
            f"  itemHighlightedBg: 33{darker_bg}",
            f"  primary: {primary_txt}",
            f"  secondary: cc{not_primary_txt}",
            f"  destructive: {not_primary_txt}",
            f"notification:",
            f"  bg: {bg}",
            f"  primaryText: {primary_txt}",
            f"  expanded:",
            f"    bgType: {dark}",
            f"    navBar:",
            f"      background: {bg}",
            f"      primaryText: {primary_txt}",
            f"      control: {not_primary_txt}",
            f"      separator: {darker_bg}",

        ]

        with open(theme, 'w') as f:
            for row in ios_data:
                f.write(str(row) + '\n')
        
        preview_bg = await self._adjust_color_brightness(hex_not_primary_txt, 0.5)
        preview = await self.create_ios_preview(
            bot_name, chat_id, image_path, preview_bg, hex_bg,
            hex_primary_txt, hex_not_primary_txt, hex_darker_bg
        )

        return theme, preview
        # return theme
