class AtRule:
    pass


class RegularAtRule:
    pass


class CharsetAtRule(RegularAtRule):
    pass


class ImportAtRule(
    RegularAtRule,
):
    pass


class NamespaceAtRule(
    RegularAtRule,
):
    pass
