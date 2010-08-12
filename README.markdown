Usage
==============

1. Add 'template_shuffle' to your INSTALLED_APPS in settings.py
2. Use the template library as shown below:
    {% load template_shuffle %}
    {% shuffle_blocks 2 %}{# this will only show 2 of the 4 possible blocks #}
        Block 1
    {% shuffle_block_separator %}
        Block 2
    {% shuffle_block_separator %}
        Block 3
    {% shuffle_block_separator %}
        {# empty block should be removed and never shown #}
    {% end_shuffle_blocks %}

