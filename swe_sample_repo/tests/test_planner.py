from starter.planner import plan

def test_placeholder_plan():
    result=plan("Sample Task")
    assert isinstance(result,list)
    assert len(result)==1
    assert "Sample Task" in result[0] # if assert condition is false then program stops suddenly