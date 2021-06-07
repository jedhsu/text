from dataclasses import dataclass
class _Patterns:
    # [TODO] finsh
    block = r"^/\* ([A-Z][A-Za-z\s]+) ([-a-z0-9]+) < ([A-Z][A-Za-z\s]+) ([-a-z0-9]+)$"
    block_snippet = r"^/\* < ([-a-z0-9]+)$"

    begin_snippet = r"^/\* < ([-a-z0-9]+)$"
    end_snippet = r"^/\* < ([-a-z0-9]+)$"

    begin_chapter = r"^\w+\*? (\w+)(;| = )"
    end_chapter = r"^\w+\*? (\w+)(;| = )"

    constructor = r"^\w+\*? (\w+)(;| = )"
    function = r"^\w+\*? (\w+)(;| = )"
    variable = r"^\w+\*? (\w+)(;| = )"
    struct = r"^struct (\w+)? {$"

    type = r"(public )?(abstract )?(class|enum|interface) ([A-Z]\w+)"

#     namedtypedef
#     unnamedtypedef
#     typedefname

class UpdateLocation:
    def update_location_before(self, line: str, index: int):
        match = re.match(Pattern.function, line)[0]
        if match and "#define" in line and match[0] in self.keywords:
            if "//" not in line and " not in line:
                is_function_declaration = line[-1] == ";"
                
                pass


            
    

@dataclass
class Parser:
    book: Book
    source: Source
    lines: Sequence[str]
    states: Sequence[ParseState]

    anonymous_typedef: Location
    location: Location
    location_before_block: Location

    def parse(self):
        for line in self.lines():
            
