import torch
import torch.nn as nn

# class MODEL(nn.Module):
#     def __init__(self):
#         super(MODEL, self).__init__()
#         self.C1 = nn.Conv1d(2, 16, 4)
#         self.C2 = nn.Conv1d(16, 16, 4)
#         self.C3 = nn.Conv1d(16, 16, 4)
#         self.pool = nn.MaxPool1d(3)
        
#         self.F1 = nn.Linear(16, 32)
#         self.F2 = nn.Linear(32, 1)
#         self.tanh = nn.Tanh()
#         self.sigmoid = nn.Sigmoid()
#         self.dropout = nn.Dropout(0.1)
#         self.attn_weights = nn.Parameter(torch.randn(78))

#     def forward(self, x):
#         attention = torch.matmul(x, self.attn_weights)
#         attention = torch.sigmoid(attention).unsqueeze(1)
#         y = (x * attention).unsqueeze(1)
        
#         x = x.unsqueeze(1)
#         x = torch.cat((x, y), dim=1)
        
#         x = self.tanh(self.C1(x))
#         x = self.pool(x)
#         x = self.dropout(x)
#         x = self.tanh(self.C2(x))
#         x = self.pool(x)
#         x = self.dropout(x)
#         x = self.tanh(self.C3(x))
#         x = self.pool(x)
#         x = self.dropout(x).squeeze(2)
#         x = self.tanh(self.F1(x))
#         x = self.dropout(x)
#         x = self.sigmoid(self.F2(x)).squeeze(1)
#         return x

from TabM import Model

class MODEL(nn.Module):
    def __init__(self, tabm):
        super(MODEL, self).__init__()
        self.tabm = tabm
        self.C1 = nn.Conv1d(10, 16, 4)
        self.C2 = nn.Conv1d(16, 16, 4)
        self.C3 = nn.Conv1d(16, 16, 4)
        self.pool = nn.MaxPool1d(3)
        self.F1 = nn.Linear(16, 32)
        self.F2 = nn.Linear(32, 1)
        self.tanh = nn.Tanh()
        self.sigmoid = nn.Sigmoid()
        self.dropout = nn.Dropout(0.1)
        self.attn_weights = nn.Parameter(torch.randn(78))

    def forward(self, x=None, x_cat=None):
        t = self.tabm(x, x_cat)
        attention = torch.matmul(x, self.attn_weights)
        attention = torch.sigmoid(attention).unsqueeze(1)
        y = (x * attention).unsqueeze(1)
        
        x = x.unsqueeze(1)
        x = torch.cat((x, y, t), dim=1)
        x = self.tanh(self.C1(x))
        x = self.pool(x)
        x = self.dropout(x)
        x = self.tanh(self.C2(x))
        x = self.pool(x)
        x = self.dropout(x)
        x = self.tanh(self.C3(x))
        x = self.pool(x)
        x = self.dropout(x).squeeze(2)
        x = self.tanh(self.F1(x))
        x = self.dropout(x)
        x = self.sigmoid(self.F2(x)).squeeze(1)
        return x

backbone_config = {
    'type': 'MLP',
    'n_blocks': 2,
    'd_block': 32,
    'dropout': 0.1,
}
tabm = Model(
    n_num_features=78,
    cat_cardinalities=[],
    n_classes=78,
    backbone=backbone_config,
    num_embeddings=None,
    arch_type='tabm',
    bins=None,
    k=8
)

model = MODEL(tabm=tabm)