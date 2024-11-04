from PySide6.QtWidgets import QStyledItemDelegate, QLineEdit, QCompleter
from PySide6.QtCore import Qt


class CompleterDelegate(QStyledItemDelegate):
    def __init__(self, words=None, parent=None):
        super(CompleterDelegate, self).__init__(parent)
        if words is None:
            self.completer_words = ["大椎", "至阳", "命门", "大杼", "肺兪", "肾兪", "百会", "神庭", "印堂", "头维", "攒竹", "迎香", "水分", "气海", "关元", "期门", "气穴", "足三里"]
        else:
            self.completer_words = words

    def createEditor(self, parent, option, index):
        # 创建 QLineEdit 作为编辑器
        editor = QLineEdit(parent)

        # 创建 QCompleter 并将其绑定到编辑器
        completer = QCompleter(self.completer_words, editor)
        # completer.setCaseSensitivity(Qt.CaseInsensitive)  # 忽略大小写
        completer.setFilterMode(Qt.MatchContains)  # 匹配模式：包含部分匹配
        editor.setCompleter(completer)

        return editor

    def setEditorData(self, editor, index):
        # 从模型中获取数据并设置到编辑器
        text = index.model().data(index, Qt.DisplayRole)
        editor.setText(text)

    def setModelData(self, editor, model, index):
        # 将编辑器中的数据保存回模型
        model.setData(index, editor.text(), Qt.EditRole)

    def updateEditorGeometry(self, editor, option, index):
        # 设置编辑器的几何形状
        editor.setGeometry(option.rect)
