from typing import Tuple

from keras import layers, losses, models, optimizers
from keras.callbacks import History
from keras.models import Sequential
from numpy.typing import NDArray


def train_model(
    dataset: Tuple[NDArray, NDArray],
    max_features=10000,
    max_len=40,
    with_summary=True,
) -> Tuple[Sequential, History]:
    """编译并训练 RNN 模型

    模型非常简单
    - 1个嵌入层，作用是？
    - 1个全连接层

    TODO

    Args:
        dataset (Tuple[NDArray, NDArray]): 训练数据集
        max_features (int, optional): 最大输入词数量. Defaults to 10000.
        max_len (int, optional): 词嵌入最大数量. Defaults to 40.
        with_summary (bool, optional): 是否在标准输出打印模型架构信息，默认输出.

    Returns:
        Tuple[Sequential, History]: 模型和模型训练的历史数据
    """
    model = models.Sequential(
        [
            layers.Input(shape=(max_len,)),
            layers.Embedding(max_features, 8),
            layers.Flatten(),
            layers.Dense(1, activation="sigmoid"),
        ]
    )

    if with_summary:
        model.summary()

    model.compile(
        optimizer=optimizers.RMSprop(),  # type: ignore
        loss=losses.BinaryCrossentropy(),
        metrics=["accuracy"],
    )

    train_x, train_y = dataset

    history = model.fit(
        x=train_x,
        y=train_y,
        epochs=10,
        batch_size=32,
        validation_split=0.2,
    )

    return model, history
