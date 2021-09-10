# _*_ coding: utf-8 _*_

"""
inst_save.py by xianhu
"""


class Saver(object):
    """
    class of Saver, must include function working()
    """

    def working(self, priority: int, url: str, keys: dict, deep: int, item: object) -> (int, object):
        """
        working function, must "try-except" and don't change the parameters and returns
        :return save_state: can be -1(save failed), 1(save success)
        :return save_result: can be any object, or exception[class_name, excep]
        """
        try:
            save_state, save_result = self.item_save(priority, url, keys, deep, item)
        except Exception as excep:
            save_state, save_result = -1, [self.__class__.__name__, excep]

        return save_state, save_result

    def item_save(self, priority: int, url: str, keys: dict, deep: int, item: object) -> (int, object):
        """
        save the content of a url. You must overwrite this function, parameters and returns refer to self.working()
        """
        raise NotImplementedError
