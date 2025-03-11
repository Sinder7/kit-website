import json

from django.contrib import admin
from django import forms
from django.utils.safestring import mark_safe

from .models import Page


"""class BlockEditorWidget(forms.Widget):
    def render(self, name, value, attrs=..., renderer=...):
        if value is None:
            value = []
        elif isinstance(value, str):
            try:
                value = json.loads(value)
            except json.JSONDecodeError:
                value = []

        html = f"
                <div id="block-editor-{name}">
                <div class="block-list">
                    <!-- Здесь будут отображаться добавленные блоки -->
                </div>
                <select class="block-type-selector">
                    <option value="">Добавить блок</option>
                    <option value="text">Текст</option>
                    <option value="image">Изображение</option>
                    <option value="video">Видео</option>
                </select>
                <button type="button" class="add-block">Добавить</button>
            </div>
            <textarea name="{name}" id="id_{name}" style="display:none;">{json.dumps(value)}</textarea>
            <script>
                (function() {{
                    var editor = document.getElementById("block-editor-{name}");
                    var textarea = document.getElementById("id_{name}");
                    var blockList = editor.querySelector(".block-list");
                    var addButton = editor.querySelector(".add-block");
                    var selector = editor.querySelector(".block-type-selector");

                    var blocks = JSON.parse(textarea.value || "[]");

                    function renderBlocks() {{
                        blockList.innerHTML = "";
                        blocks.forEach(function(block, index) {{
                            var div = document.createElement("div");
                            div.className = "block-item";
                            div.innerHTML = "<strong>" + block.type + "</strong>: " + block.value + 
                                ' <button type="button" data-index="' + index + '" class="remove-block">Удалить</button>';
                            blockList.appendChild(div);
                        }});
                        textarea.value = JSON.stringify(blocks);
                    }}

                    addButton.addEventListener("click", function() {{
                        var blockType = selector.value;
                        if (!blockType) return;
                        var blockValue = prompt("Введите содержимое для блока " + blockType + ":");
                        if (blockValue === null) return;
                        blocks.push({{type: blockType, value: blockValue}});
                        renderBlocks();
                    }});

                    blockList.addEventListener("click", function(e) {{
                        if (e.target.classList.contains("remove-block")) {{
                            var index = e.target.getAttribute("data-index");
                            blocks.splice(index, 1);
                            renderBlocks();
                        }}
                    }});

                    renderBlocks();
                }})();
            </script>
            <style>
                #block-editor-{name} .block-list {{
                    margin-bottom: 10px;
                }}
                #block-editor-{name} .block-item {{
                    border: 1px solid #ccc;
                    padding: 5px;
                    margin-bottom: 5px;
                }}
            </style>
            "

        return mark_safe(html)


class PageAdminForm(forms.ModelForm):
    class Meta:
        model = Page
        fields = "__all__"
        widget = {"content": BlockEditorWidget()}
"""

@admin.register(Page)
class PageAdmin(admin.ModelAdmin):
    list_display = ("title", "parent")
    prepopulated_fields = {"slug": ("title",)}


