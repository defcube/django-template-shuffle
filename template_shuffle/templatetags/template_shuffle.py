from django import template
import random
register = template.Library()

class ShuffleNode(template.Node):
    def __init__(self, blocks, max_nodes=None):
        if max_nodes:
            self.max_nodes = int(max_nodes)
        else:
            self.max_nodes = None
        self.blocks = blocks
    
    def render(self, context):
        blocks = list(self.blocks)
        random.shuffle(blocks)
        output = ""
        num_blocks_rendered = 0
        for block in blocks:
            block_output = block.render(context)
            output += block_output
            if block_output.strip() != "":
                num_blocks_rendered += 1
            if self.max_nodes and num_blocks_rendered == self.max_nodes:
                break
        return output

@register.tag('shuffle_blocks')
def do_shuffle_blocks(parser, token):
    blocks = []
    bits = token.split_contents()
    if len(bits) > 2:
        raise template.TemplateSyntaxError("shuffle_blocks [max_blocks]")
    elif len(bits) == 2:
        max_blocks = bits[1]
    elif len(bits) == 1:
        max_blocks = None
    while True:
        nodelist = parser.parse(('end_shuffle_blocks', 
                                 'shuffle_block_separator'))
        blocks.append(nodelist)
        token = parser.next_token()
        if token.contents == 'end_shuffle_blocks':
            break
    return ShuffleNode(blocks, max_nodes=max_blocks)
    